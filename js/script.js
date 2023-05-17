function carregarOpcoesRacas(idSelect) {
  const select = document.getElementById(idSelect);

  fetch("../data/races.json")
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

  fetch("../data/subRaces.json")
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

  fetch("../data/backgrounds.json")
    .then((response) => response.json())
    .then((data) => {
      data.background.forEach((background) => {
        const option = document.createElement("option");
        option.text = `${background.name} (${background.source})`;
        select.add(option);
      });
    });
}

function atualizarAtributos(raceName, subraceName) {
  fetch("../data/races.json")
    .then((response) => response.json())
    .then((data) => {
      let race;

      if (Array.isArray(data) && data.length > 0) {
        const filteredData = data.filter((race) => race.name === raceName);
        race = filteredData[0];

        if (race) {
          let attributes = {};

          if (subraceName) {
            const subrace = race.subrace.find((subrace) => subrace.name === subraceName);
            if (subrace && subrace.ability) {
              attributes = { ...race.ability, ...subrace.ability };
            } else {
              attributes = race.ability;
            }
          } else {
            attributes = race.ability;
          }

          if (attributes && Object.keys(attributes).length > 0) {
            const bonusTextDiv = document.getElementById("bonus-text");
            bonusTextDiv.innerHTML = "";
          
            if (attributes.choose) {
              const { choose, ...remainingAttributes } = attributes;
              const chooseOptions = choose.from.map((option) => {
                const value = remainingAttributes[option];
                return `${option} + ${value}`;
              });
              bonusTextDiv.textContent = `Escolha entre: ${chooseOptions.join(", ")}`;
            } else {
              const bonusText = Object.entries(attributes)
                .filter(([_, value]) => value !== 0)
                .map(([attribute, value]) => `${attribute} + ${value}`)
                .join(" ");
              bonusTextDiv.textContent = bonusText;
            }
          } else {
            const bonusTextDiv = document.getElementById("bonus-text");
            bonusTextDiv.textContent = "Atributos não encontrados";
          }
        } else {
          console.error("Raça não encontrada no arquivo JSON");
        }
      } else {
        console.error("O arquivo JSON não contém dados válidos");
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
    if (raceName) {
      atualizarAtributos(raceName);
    } else {
      const bonusTextDiv = document.getElementById("bonus-text");
      bonusTextDiv.textContent = "";
    }
  });

  carregarOpcoesRacas("race-select");
  carregarOpcoesSubracas(raceSelect.value.split(" (")[0], "subrace-select");
  carregarOpcoesBackgrounds("background-select");

  const initialRaceName = raceSelect.value.split(" (")[0];
  if (initialRaceName) {
    atualizarAtributos(initialRaceName);
  }
});
