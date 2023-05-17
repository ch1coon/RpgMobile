function carregarOpcoesRacas(idSelect) {
  const select = document.getElementById(idSelect);

  fetch("../data/races.json")
    .then((response) => response.json())
    .then((data) => {
      const uniqueRaces = new Set();

      data.race.forEach((race) => {
        if (!race.traitTags || !race.traitTags.includes("NPC Race")) {
          const raceName = race.name;
          if (!raceName.includes("(")) {
            uniqueRaces.add(raceName);
          }
        }
      });



      uniqueRaces.forEach((raceName) => {
        const option = document.createElement("option");
        option.text = raceName;
        select.add(option);
      });
    })
    .catch((error) => {
      //console.error("Erro ao carregar o JSON races.json:", error);
    });
}


carregarOpcoesRacas("race-select");

function carregarOpcoesSubracas() {
  const raceSelect = document.getElementById("race-select");
  const subraceSelect = document.getElementById("subraces-select");

  if (!subraceSelect) {
    console.error("Elemento subraces-select não encontrado.");
    return;
  }

  const selectedRace = raceSelect.value;

  fetch("../data/races.json")
    .then((response) => response.json())
    .then((data) => {
      const race = data.race.find((entry) => entry.name === selectedRace);

      if (race && race.subrace) {
        subraceSelect.innerHTML = ""; // Limpar as opções existentes

        race.subrace.forEach((subrace) => {
          const option = document.createElement("option");
          option.text = `${subrace.name} (${subrace.source})`;
          subraceSelect.add(option);
        });
      }
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
      const races = data.race.filter((entry) => entry.name === raceName);

      if (races.length > 0) {
        let selectedRace = null;
        const selectedSource = races.length > 1 ? getSelectedSource() : null;

        if (selectedSource) {
          selectedRace = races.find((entry) => entry.source === selectedSource);
        } else {
          selectedRace = races.find((entry) => !entry.source || entry.source !== "NPC Race");
        }

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
      } else {
        console.error("Raça não encontrada no arquivo JSON");
      }
    })
    .catch((error) => {
      console.error("Erro ao carregar o JSON races.json:", error);
    });
}

function getSelectedSource() {
  const sourceSelect = document.getElementById("source-select");
  return sourceSelect.value;
}







document.addEventListener("DOMContentLoaded", () => {
  const raceSelect = document.getElementById("race-select");
  const subraceSelect = document.getElementById("subraces-select");
  const backgroundSelect = document.getElementById("background-select");

  raceSelect.addEventListener("change", () => {
  const raceName = raceSelect.value.split(" (")[0];
  carregarOpcoesSubracas(raceName, "subraces-select");
  if (raceName) {
    atualizarAtributos(raceName);
  } else {
    const bonusTextDiv = document.getElementById("bonus-text");
    bonusTextDiv.textContent = "";
  }
});


  carregarOpcoesRacas("race-select");
  carregarOpcoesSubracas(raceSelect.value.split(" (")[0], "subraces-select");
  carregarOpcoesBackgrounds("background-select");

  const initialRaceName = raceSelect.value.split(" (")[0];
  if (initialRaceName) {
    atualizarAtributos(initialRaceName);
  }
});
