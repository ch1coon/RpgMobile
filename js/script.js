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

function carregarOpcoesSubracas(selectedRaceName) {
  const raceSelect = document.getElementById("race-select");
  const subraceSelect = document.getElementById("subraces-select");

  if (!subraceSelect) {
    console.error("Elemento subraces-select não encontrado.");
    return;
  }
 

  fetch("../data/races.json")
    .then((response) => response.json())
    .then((data) => {
      const matchingRaces = data.race.filter((race) => race.name.includes(selectedRaceName));

      const matchingSubraces = data.subrace.filter((subrace) => subrace.raceName.includes(selectedRaceName));

      subraceSelect.innerHTML = ""; // Limpar as opções existentes

      matchingRaces.forEach((race) => {
        const option = document.createElement("option");
        option.text = `${race.name} (${race.source})`;
        subraceSelect.add(option);
      });

      matchingSubraces.forEach((subrace) => {
        const option = document.createElement("option");
        if (!subrace.name) {
          option.text = `${subrace.raceName} (base)`;
        } else {
          option.text = `${subrace.name} (${subrace.source})`;
        }
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

function atualizarAtributos(selectedSubrace) {
  fetch("../data/races.json")
    .then((response) => response.json())
    .then((data) => {
      let selectedData;

      if (selectedSubrace.includes("race")) {
        const selectedRaceName = selectedSubrace.split(" (")[0];
        selectedData = data.race.find((race) => race.name === selectedRaceName);
      } else if (selectedSubrace.includes("subrace")) {
        const selectedSubraceName = selectedSubrace.split(" (")[0];
        selectedData = data.subrace.find((subrace) => subrace.name === selectedSubraceName);
      }

      if (!selectedData) {
        console.error("Raça ou subraça não encontrada no arquivo JSON");
        return;
      }

      if (selectedData.ability) {
        const bonusTextDiv = document.getElementById("bonus-text");
        bonusTextDiv.textContent = "";
        const abilities = selectedData.ability[0];
        const bonusText = Object.entries(abilities)
          .map(([attribute, value]) => `${attribute}: +${value}`)
          .join(", ");
        bonusTextDiv.textContent = bonusText;
      } else if (selectedData.lineage === "UA1") {
        const bonusTextDiv = document.getElementById("bonus-text");
        bonusTextDiv.textContent = "";

        const selectGroup = document.createElement("div");
        selectGroup.className = "row";

        const select1 = document.createElement("select");
        select1.className = "form-select col";
        select1.innerHTML = `
          <option value="strength">+2</option>
          <option value="dexterity">+2</option>
          <option value="constitution">+2</option>
          <option value="intelligence">+2</option>
          <option value="wisdom">+2</option>
          <option value="charisma">+2</option>
        `;
        selectGroup.appendChild(select1);

        const select2 = document.createElement("select");
        select2.className = "form-select col";
        select2.innerHTML = `
          <option value="strength">+1</option>
          <option value="dexterity">+1</option>
          <option value="constitution">+1</option>
          <option value="intelligence">+1</option>
          <option value="wisdom">+1</option>
          <option value="charisma">+1</option>
        `;
        selectGroup.appendChild(select2);

        bonusTextDiv.appendChild(selectGroup);
      } else if (selectedData.lineage === "VRGR") {
        const bonusTextDiv = document.getElementById("bonus-text");
        bonusTextDiv.textContent = "";

        const selectGroup = document.createElement("div");
        selectGroup.className = "row";

        const select1 = document.createElement("select");
        select1.className = "form-select col";
        select1.innerHTML = `
          <option value="+2|+1">+2|+1</option>
          <option value="+1|+1|+1">+1|+1|+1</option>
        `;
        selectGroup.appendChild(select1);

        bonusTextDiv.appendChild(selectGroup);

        select1.addEventListener("change", (event) => {
          const selectedValue = event.target.value;
          const values = selectedValue.split("|");
          const selectGroup = document.createElement("div");
          selectGroup.className = "row";

          values.forEach((value) => {
            const select = document.createElement("select");
            select.className = "form-select col";
            select.innerHTML = `
              <option value="strength">+${value}</option>
              <option value="dexterity">+${value}</option>
              <option value="constitution">+${value}</option>
              <option value="intelligence">+${value}</option>
              <option value="wisdom">+${value}</option>
              <option value="charisma">+${value}</option>
            `;
            selectGroup.appendChild(select);
          });

          bonusTextDiv.appendChild(selectGroup);
        });
      } else {
        console.log("É uma cópia");
      }
    })
    .catch((error) => {
      console.error("Erro ao carregar o JSON races.json:", error);
    });
}



function criarSelectsUA1(selectedSubrace) {
  const selectContainer = document.getElementById("select-container");
  selectContainer.innerHTML = ""; // Limpar o conteúdo existente

  const select1 = document.createElement("select");
  select1.classList.add("form-select", "mb-3");
  const select2 = document.createElement("select");
  select2.classList.add("form-select", "mb-3");

  const options = [
    "Escolha qualquer",
    "Escolha qualquer outro",
    "Strength",
    "Dexterity",
    "Constitution",
    "Intelligence",
    "Wisdom",
    "Charisma",
  ];

  options.forEach((option) => {
    const option1 = document.createElement("option");
    option1.value = option;
    option1.textContent = option;
    select1.appendChild(option1);

    const option2 = document.createElement("option");
    option2.value = option;
    option2.textContent = option;
    select2.appendChild(option2);
  });

  selectContainer.appendChild(select1);
  selectContainer.appendChild(select2);

  select1.addEventListener("change", () => {
    select2.querySelector(`option[value="${select1.value}"]`).disabled = true;
  });

  select2.addEventListener("change", () => {
    select1.querySelector(`option[value="${select2.value}"]`).disabled = true;
  });
}

function criarSelectsVRGR(selectedSubrace) {
  const selectContainer = document.getElementById("select-container");
  selectContainer.innerHTML = ""; // Limpar o conteúdo existente

  const select = document.createElement("select");
  select.classList.add("form-select", "mb-3");

  const options = ["+2|+1", "+1|+1|+1"];

  options.forEach((option) => {
    const optionElement = document.createElement("option");
    optionElement.value = option;
    optionElement.textContent = option;
    select.appendChild(optionElement);
  });

  selectContainer.appendChild(select);

  select.addEventListener("change", () => {
    const selectedOption = select.value;

    if (selectedOption === "+2|+1") {
      criarSelectsVRGRAttributes("+2", "+1");
    } else if (selectedOption === "+1|+1|+1") {
      criarSelectsVRGRAttributes("+1", "+1", "+1");
    }
  });
}

function criarSelectsVRGRAttributes(attribute1, attribute2, attribute3) {
  const selectContainer = document.getElementById("select-container");
  selectContainer.innerHTML = ""; // Limpar o conteúdo existente

  const select1 = document.createElement("select");
  select1.classList.add("form-select", "mb-3");
  const select2 = document.createElement("select");
  select2.classList.add("form-select", "mb-3");

  const attributes = [
    "Strength",
    "Dexterity",
    "Constitution",
    "Intelligence",
    "Wisdom",
    "Charisma",
  ];

  attributes.forEach((attribute) => {
    const option1 = document.createElement("option");
    option1.value = attribute;
    option1.textContent = `${attribute} ${attribute1}`;
    select1.appendChild(option1);

    const option2 = document.createElement("option");
    option2.value = attribute;
    option2.textContent = `${attribute} ${attribute2}`;
    select2.appendChild(option2);
  });

  selectContainer.appendChild(select1);
  selectContainer.appendChild(select2);

  select1.addEventListener("change", () => {
    select2.querySelector(`option[value="${select1.value}"]`).disabled = true;
  });

  select2.addEventListener("change", () => {
    select1.querySelector(`option[value="${select2.value}"]`).disabled = true;
  });
}






document.addEventListener("DOMContentLoaded", () => {
  const raceSelect = document.getElementById("race-select");
  const subraceSelect = document.getElementById("subraces-select");
  const backgroundSelect = document.getElementById("background-select");
  const abilityScore_STR = document.getElementById("strength");
  const abilityScore_DEX = document.getElementById("dexterity");
  const abilityScore_CON = document.getElementById("constitution");
  const abilityScore_INT = document.getElementById("intelligence");
  const abilityScore_WIS = document.getElementById("wisdom");
  const abilityScore_CHA = document.getElementById("charisma");

  raceSelect.addEventListener("change", () => {
    const selectedRaceName = raceSelect.value.split(" (")[0];
    carregarOpcoesSubracas(selectedRaceName, "subraces-select");
    if (selectedRaceName) {
      
    } else {
      const bonusTextDiv = document.getElementById("bonus-text");
      bonusTextDiv.textContent = "";
    }
  });

  subraceSelect.addEventListener("change", () => {
    const selectedSubrace = subraceSelect.value;
    if (selectedSubrace) {
      atualizarAtributos(selectedSubrace);
    } else {
      const bonusTextDiv = document.getElementById("bonus-text");
      bonusTextDiv.textContent = "";
    }
  });
  

  carregarOpcoesRacas("race-select");
  carregarOpcoesBackgrounds("background-select");

  const initialRaceName = raceSelect.value.split(" (")[0];
  if (initialRaceName) {
    
  }
});

