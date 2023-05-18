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

      const matchingSubraces = data.subrace.filter((subrace) => subrace.raceName === selectedRaceName);



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


function criarSelectsUA1(selectedSubrace) {
  const selectContainer = document.getElementById("select-container");
  selectContainer.innerHTML = ""; // Limpar o conteúdo existente

  const select1 = document.createElement("select");
  select1.classList.add("form-select", "mb-3");
  const select2 = document.createElement("select");
  select2.classList.add("form-select", "mb-3");

  const options = [
    "Strength",
    "Dexterity",
    "Constitution",
    "Intelligence",
    "Wisdom",
    "Charisma",
  ];

  // Adicionar opção "+2" ao primeiro select
  const optionPlus2 = document.createElement("option");
  optionPlus2.value = "+2";
  optionPlus2.textContent = "+2";
  optionPlus2.selected = true; // Selecionar a opção
  optionPlus2.disabled = true; // Desativar a opção
  select1.appendChild(optionPlus2);

  options.forEach((option) => {
    const option1 = document.createElement("option");
    option1.value = option;
    option1.textContent = option;
    select1.appendChild(option1);
  });

  // Adicionar opção "+1" ao segundo select
  const optionPlus2Select2 = document.createElement("option");
  optionPlus2Select2.value = "+1";
  optionPlus2Select2.textContent = "+1";
  optionPlus2Select2.selected = true; // Selecionar a opção
  optionPlus2Select2.disabled = true; // Desativar a opção
  select2.appendChild(optionPlus2Select2);

  options.forEach((option) => {
    const option2 = document.createElement("option");
    option2.value = option;
    option2.textContent = option;
    select2.appendChild(option2);
  });

  selectContainer.appendChild(select1);
  selectContainer.appendChild(select2);

  let previousOptionSelect1 = optionPlus2; // Armazenar a opção anterior selecionada do select 1
  let previousOptionSelect2 = optionPlus2Select2; // Armazenar a opção anterior selecionada do select 2

  let selectedOption2 = null;

  select1.addEventListener("change", () => {
    const selectedValue = select1.value;
  
    // Reativar todas as opções do select2
    select2.querySelectorAll('option').forEach((option, index) => {
      option.disabled = false;
      if (index === 0) {
        option.disabled = true; // Desativar a primeira opção do select2
      }
    });
  
    // Desativar a opção selecionada no select2
    select2.querySelector(`option[value="${selectedValue}"]`).disabled = true;
  
    // Verificar se a opção selecionada no select2 é a mesma do select1
    if (selectedOption2 === selectedValue || selectedValue === "+2") {
      selectedOption2 = null; // Limpar a seleção no select2
      select2.value = ''; // Limpar a seleção visualmente no select2
    }
  });
  
  select2.addEventListener("change", () => {
    const selectedValue = select2.value;
  
    // Reativar todas as opções do select1
    select1.querySelectorAll('option').forEach((option, index) => {
      option.disabled = false;
      if (index === 0) {
        option.disabled = true; // Desativar a primeira opção do select1
      }
    });
  
    // Desativar a opção selecionada no select1
    select1.querySelector(`option[value="${selectedValue}"]`).disabled = true;
  
    selectedOption2 = selectedValue;
  });
  
  




  const bonusTextDiv = document.getElementById("bonus-text");
  bonusTextDiv.disabled = true;
}

function criarSelectsVRGR(selectedSubrace) {
  const selectContainer = document.getElementById("select-container");
  selectContainer.textContent = ""; // Limpar o conteúdo existente

  const select = document.createElement("select");
  select.id = "VRGROptions";
  select.classList.add("form-select", "mb-3");

  const options = ["+2|+1", "+1|+1|+1"];

    // Adicionar opção "escolha um opção:" ao primeiro select
    const pointOptions = document.createElement("option");
    pointOptions.value = "escolha um opção:";
    pointOptions.textContent = "escolha um opção:";
    pointOptions.selected = true; // Selecionar a opção
    pointOptions.disabled = true; // Desativar a opção
    select.appendChild(pointOptions);

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
      criarSelectsVRGR21("+2", "+1");
    } else if (selectedOption === "+1|+1|+1") {
      //criarSelectsVRGRAttributes("+1", "+1", "+1");
    }
  });
}



function criarSelectsVRGR21(selectedSubrace) {
  const selectContainer = document.getElementById("select-container");

// Verifica se selectContainer existe
if (selectContainer) {
  // Obtém todos os filhos de selectContainer
  const children = Array.from(selectContainer.children);

  // Itera pelos filhos e remove aqueles que não possuem o ID desejado
  children.forEach((child) => {
    if (child.id !== "VRGROptions") {
      selectContainer.removeChild(child);
    }
  });
}

  const attribute1 = document.createElement("select");
  attribute1.classList.add("form-select", "mb-3");
  const attribute2 = document.createElement("select");
  attribute2.classList.add("form-select", "mb-3");

  const options = [
    "Strength",
    "Dexterity",
    "Constitution",
    "Intelligence",
    "Wisdom",
    "Charisma",
  ];

  // Adicionar opção "+2" ao primeiro select
  const optionPlus2 = document.createElement("option");
  optionPlus2.value = "+2";
  optionPlus2.textContent = "+2";
  optionPlus2.selected = true; // Selecionar a opção
  optionPlus2.disabled = true; // Desativar a opção
  attribute1.appendChild(optionPlus2);

  options.forEach((option) => {
    const option1 = document.createElement("option");
    option1.value = option;
    option1.textContent = option;
    attribute1.appendChild(option1);
  });

  // Adicionar opção "+1" ao segundo select
  const optionPlus2Select2 = document.createElement("option");
  optionPlus2Select2.value = "+1";
  optionPlus2Select2.textContent = "+1";
  optionPlus2Select2.selected = true; // Selecionar a opção
  optionPlus2Select2.disabled = true; // Desativar a opção
  attribute2.appendChild(optionPlus2Select2);

  options.forEach((option) => {
    const option2 = document.createElement("option");
    option2.value = option;
    option2.textContent = option;
    attribute2.appendChild(option2);
  });

  selectContainer.appendChild(attribute1);
  selectContainer.appendChild(attribute2);

  let previousOptionSelect1 = optionPlus2; // Armazenar a opção anterior selecionada do select 1
  let previousOptionSelect2 = optionPlus2Select2; // Armazenar a opção anterior selecionada do select 2

  let selectedOption2 = null;

  attribute1.addEventListener("change", () => {
    const selectedValue = attribute1.value;
  
    // Reativar todas as opções do select2
    attribute2.querySelectorAll('option').forEach((option, index) => {
      option.disabled = false;
      if (index === 0) {
        option.disabled = true; // Desativar a primeira opção do select2
      }
    });
  
    // Desativar a opção selecionada no select2
    attribute2.querySelector(`option[value="${selectedValue}"]`).disabled = true;
  
    // Verificar se a opção selecionada no select2 é a mesma do select1
    if (selectedOption2 === selectedValue || selectedValue === "+2") {
      selectedOption2 = null; // Limpar a seleção no select2
      attribute2.value = ''; // Limpar a seleção visualmente no select2
    }
  });
  
  attribute2.addEventListener("change", () => {
    const selectedValue = attribute2.value;
  
    // Reativar todas as opções do select1
    attribute1.querySelectorAll('option').forEach((option, index) => {
      option.disabled = false;
      if (index === 0) {
        option.disabled = true; // Desativar a primeira opção do select1
      }
    });
  
    // Desativar a opção selecionada no select1
    attribute1.querySelector(`option[value="${selectedValue}"]`).disabled = true;
  
    selectedOption2 = selectedValue;
  });
  
  




  const bonusTextDiv = document.getElementById("bonus-text");
  bonusTextDiv.disabled = true;
}






function atualizarAtributos(selectedSubrace) {
  fetch("../data/races.json")
    .then((response) => response.json())
    .then((data) => {
      console.log("Seleção:", selectedSubrace);

      let selectedData;

      if (selectedSubrace.includes("race")) {
        const selectedRaceName = selectedSubrace.split(" (")[0];
        selectedData = data.race.find((race) => race.name === selectedRaceName);
        console.log("Raça selecionada:", selectedRaceName);
      } else if (selectedSubrace.includes("subrace")) {
        const selectedSubraceName = selectedSubrace.split(" (")[0];
        selectedData = data.subrace.find((subrace) => subrace.name === selectedSubraceName);
        console.log("Subraça selecionada:", selectedSubraceName);
      }

      if (!selectedData) {
        const matchingRace = data.race.find((race) => race.name.includes(selectedSubrace));
        if (matchingRace) {
          selectedData = matchingRace;
          console.log("Raça selecionada:", matchingRace.name);
        } else {
          const matchingSubrace = data.subrace.find((subrace) => subrace.name.includes(selectedSubrace));
          if (matchingSubrace) {
            selectedData = matchingSubrace;
            console.log("Subraça selecionada:", matchingSubrace.name);
          }
        }
      }

      if (!selectedData) {
        console.error("Raça ou subraça não encontrada no arquivo JSON");
        console.log("Raça ou subraça selecionada:", selectedSubrace);
        console.log("Raças disponíveis:", data.race.map((race) => race.name));
        console.log("Subraças disponíveis:", data.subrace.map((subrace) => subrace.name));
        return;
      }

      console.log("passou");
      const bonusTextDiv = document.getElementById("bonus-text");
      const selectContainer = document.getElementById("select-container");

      if (selectedData.hasOwnProperty("ability")) {
        bonusTextDiv.textContent = JSON.stringify(selectedData.ability, (key, value) => {
          if (typeof value === 'object' && Object.keys(value).length === 0) {
            return '';
          }
          return value;
        });
        selectContainer.textContent = ""; // Limpar o conteúdo existente
      } else if (selectedData.hasOwnProperty("lineage")) {
        const lineage = selectedData.lineage;
        selectContainer.textContent = ""; // Limpar o conteúdo existente

        if (lineage === "UA1") {
          // Código para criar os dois selects com +2 e +1
          criarSelectsUA1(selectedSubrace);
        } else if (lineage === "VRGR") {
          // Código para criar o select com as opções "+2|+1" e "+1|+1|+1"
          criarSelectsVRGR(selectedSubrace);
        }
      } else {
        console.log("É uma cópia");
        selectContainer.textContent = ""; // Limpar o conteúdo existente
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
      ;
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

