function carregarOpcoesRacas(idSelect) {
    const select = document.getElementById(idSelect);
  
    fetch("/data/races.json")
      .then((response) => response.json())
      .then((data) => {
        data.race.forEach((race) => {
          const option = document.createElement("option");
          option.text = `${race.name} (${race.source})`;
          select.add(option);
        });
      });
  }
  
  function carregarOpcoesSubracas(raceName, idSelect) {
    const select = document.getElementById(idSelect);
    select.innerHTML = "";
  
    fetch("/data/subRaces.json")
      .then((response) => response.json())
      .then((data) => {
        const subraces = data.subrace.filter(
          (subrace) => subrace.raceName === raceName
        );
        if (subraces.length > 0) {
          subraces.forEach((subrace) => {
            const option = document.createElement("option");
            option.text = `${subrace.name} (${subrace.source})`;
            select.add(option);
          });
          select.style.display = "block";
        } else {
          select.style.display = "none";
        }
      });
  }
  
  function carregarOpcoesBackgrounds(idSelect) {
    const select = document.getElementById(idSelect);
  
    fetch("/data/backgrounds.json")
      .then((response) => response.json())
      .then((data) => {
        data.background.forEach((background) => {
          const option = document.createElement("option");
          option.text = `${background.name} (${background.source})`;
          select.add(option);
        });
      });
  }
  
  function atualizarAtributos(raceName) {
    fetch("/data/races.json")
      .then((response) => response.json())
      .then((data) => {
        const race = data.race.find((race) => race.name === raceName);
  
        if (race) {
          const bonusTextDiv = document.getElementById("bonus-text");
          let bonusText = "";
  
          if (race.ability && race.ability.choose) {
            bonusText += "Escolha entre: ";
  
            // Remove os botões existentes antes de adicionar os novos
            bonusTextDiv.innerHTML = "";
  
            race.ability.choose.forEach((attribute) => {
              const value = race.ability[attribute];
              if (value !== undefined) {
                const button = document.createElement("button");
                button.textContent = `${attribute} + ${value}`;
                button.addEventListener("click", () => {
                  bonusTextDiv.textContent = `${attribute} + ${value}`;
                });
                bonusTextDiv.appendChild(button);
              }
            });
          } else {
            for (const attribute in race.ability) {
              const value = race.ability[attribute];
              if (value !== undefined && value !== 0) {
                bonusText += `${attribute} + ${value} `;
              }
            }
  
            bonusTextDiv.textContent = bonusText.trim();
          }
        } else {
          const bonusTextDiv = document.getElementById("bonus-text");
          bonusTextDiv.textContent = "Raça inválida";
        }
      })
      .catch((error) => {
        console.error("Erro ao carregar o JSON races.json:", error);
      });
  }
  
  
  
  
  
  document.addEventListener("DOMContentLoaded", () => {
    const raceSelect = document.getElementById("race-select");
    const subraceSelect = document.getElementById("subrace-select");
    const backgroundSelect = document.getElementById("background-select");
  
    raceSelect.addEventListener("change", () => {
      const raceName = raceSelect.value.split(" (")[0];
      carregarOpcoesSubracas(raceName, "subrace-select");
      atualizarAtributos(raceName);
    });
  
    carregarOpcoesRacas("race-select");
    carregarOpcoesSubracas(raceSelect.value.split(" (")[0], "subrace-select");
    carregarOpcoesBackgrounds("background-select");
  
    atualizarAtributos(raceSelect.value.split(" (")[0]);
  });
  