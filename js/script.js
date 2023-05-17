function carregarOpcoesRacas() {
  fetch("../data/races.json")
    .then((response) => response.json())
    .then((data) => {
      const raceSelect = document.getElementById("race-select");
      const uniqueRaces = new Set();

      data.race.forEach((race) => {
        const raceName = race.name.replace(/\s*\([^)]*\)/g, "").trim(); // Remover conteúdo entre parênteses
        if (!uniqueRaces.has(raceName) && (!race.traitTags || !race.traitTags.includes("NPC Race"))) {
          uniqueRaces.add(raceName);
          const option = document.createElement("option");
          option.value = raceName;
          option.text = raceName;
          raceSelect.appendChild(option);
        }
      });

      raceSelect.addEventListener("change", () => {
        const selectedRaceName = raceSelect.value;
        carregarOpcoesSubracas(selectedRaceName);
        if (selectedRaceName) {
          atualizarAtributos(selectedRaceName);
        } else {
          const bonusTextDiv = document.getElementById("bonus-text");
          bonusTextDiv.textContent = "";
        }
      });
    })
    .catch((error) => {
      console.error("Erro ao carregar o JSON races.json:", error);
    });
}


function carregarOpcoesSubracas(selectedRaceName, selectId) {
  const subraceSelect = document.getElementById(selectId);

  if (!subraceSelect) {
    console.error("Elemento subraces-select não encontrado.");
    return;
  }

  fetch("../data/races.json")
    .then((response) => response.json())
    .then((data) => {
      const selectedRace = data.race.find((race) => race.name === selectedRaceName);

      if (!selectedRace) {
        console.error("Raça não encontrada no arquivo JSON");
        return;
      }

      const races = [selectedRace];
      if (selectedRace.subrace) {
        races.push(...selectedRace.subrace);
      }

      subraceSelect.innerHTML = ""; // Limpar as opções existentes

      races.forEach((race) => {
        const option = document.createElement("option");
        option.text = `${race.name} (${race.source})`;
        subraceSelect.add(option);
      });
    })
    .catch((error) => {
      console.error("Erro ao carregar o JSON races.json:", error);
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
      const selectedRace = data.race.find((race) => race.name === raceName);

      if (!selectedRace) {
        console.error("Raça não encontrada no arquivo JSON");
        return;
      }

      let attributes = {};

      if (subraceName) {
        const subrace = selectedRace.subrace.find((subrace) => subrace.name === subraceName);
        if (subrace) {
          if (subrace.ability) {
            attributes = { ...subrace.ability[0] };
          } else if (subrace.lineage === "VRGR") {
            attributes = {
              choose: {
                from: ["Escolha qualquer", "Escolha qualquer outro"],
                count: 2,
                amount: 2
              }
            };
          } else if (subrace.lineage === "UA1") {
            attributes = {
              choose: {
                from: ["Escolha qualquer", "Escolha qualquer outro"],
                count: 2,
                amount: 1
              }
            };
          }
        } else {
          console.error("Subraça não encontrada para a raça informada");
        }
      } else {
        if (selectedRace.ability) {
          attributes = { ...selectedRace.ability[0] };
        } else if (selectedRace.lineage === "VRGR") {
          attributes = {
            choose: {
              from: ["Escolha qualquer", "Escolha qualquer outro"],
              count: 2,
              amount: 2
            }
          };
        } else if (selectedRace.lineage === "UA1") {
          attributes = {
            choose: {
              from: ["Escolha qualquer", "Escolha qualquer outro"],
              count: 2,
              amount: 1
            }
          };
        }
      }

      if (attributes && Object.keys(attributes).length > 0) {
        const bonusTextDiv = document.getElementById("bonus-text");
        bonusTextDiv.innerHTML = "";

        if (attributes.choose) {
          if (attributes.choose === "VRGR") {
            bonusTextDiv.textContent = "Escolha uma das seguintes opções: (a) Escolha qualquer +2; escolha qualquer outro +1 ou (b) Escolha três diferentes +1";
          } else if (attributes.choose === "UA1") {
            bonusTextDiv.textContent = "Escolha qualquer +2; escolha qualquer outro +1";
          } else {
            const { choose, ...remainingAttributes } = attributes;
            const chooseOptions = choose.from.map((option) => {
              const value = remainingAttributes[option];
              return `${option} + ${value}`;
            });
            bonusTextDiv.textContent = `Escolha entre: ${chooseOptions.join(", ")}`;
          }
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
    })
    .catch((error) => {
      console.error("Erro ao carregar o JSON races.json:", error);
    });
}

document.addEventListener("DOMContentLoaded", () => {
  const raceSelect = document.getElementById("race-select");
  const subraceSelect = document.getElementById("subraces-select");
  const backgroundSelect = document.getElementById("background-select");

  raceSelect.addEventListener("change", () => {
    const selectedRaceName = raceSelect.value.split(" (")[0];
    carregarOpcoesSubracas(selectedRaceName, "subraces-select");
    if (selectedRaceName) {
      atualizarAtributos(selectedRaceName);
    } else {
      const bonusTextDiv = document.getElementById("bonus-text");
      bonusTextDiv.textContent = "";
    }
  });

  carregarOpcoesRacas("race-select");
  carregarOpcoesBackgrounds("background-select");

  const initialRaceName = raceSelect.value.split(" (")[0];
  if (initialRaceName) {
    atualizarAtributos(initialRaceName);
  }
});
