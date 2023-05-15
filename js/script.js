function carregarOpcoes(races, idSelect) {
  const select = document.getElementById(idSelect);

  fetch('/data/races.json')
    .then(response => response.json())
    .then(data => {
      data.race.forEach(race => {
        const option = document.createElement('option');
        option.text = `${race.name} (${race.source})`;
        select.add(option);
      });
    });
}

function carregarOpcoesSubracas(raceName, idSelect) {
  const select = document.getElementById(idSelect);
  select.innerHTML = '';

  fetch('/data/subraces.json')
    .then(response => response.json())
    .then(data => {
      const subraces = data.subrace.filter(subrace => subrace.raceName === raceName);
      if (subraces.length > 0) {
        subraces.forEach(subrace => {
          const option = document.createElement('option');
          option.text = `${subrace.name} (${subrace.source})`;
          select.add(option);
        });
        select.style.display = 'block';
      } else {
        select.style.display = 'none';
      }
    });
}

// function carregarOpcoesClasses(id){
//     let select = document.getElementById(id);

//     fetch('static/data/class')
//         .then(response => response.json())
//         .then(data => {
//             let classes = data.classes;
	
//             for (let i = 0; i < classes.length; i++) {
//                 let option = document.createElement('option');
//                 let nomeArquivo = classes[i].name.toLowerCase().replace(/ /g,"_") + '.class';
//                 fetch('classes/' + nomeArquivo)
//                     .then(response => {
//                         if(response.ok){
//                             option.value = classes[i].name;
//                             option.innerHTML = classes[i].name;
//                             select.appendChild(option);
//                         } else {
//                             console.log('O arquivo ' + nomeArquivo + ' não é de classe');
//                         }
//                     })
//                     .catch(error => console.log('Erro ao buscar arquivo: ' + error.message));
//             }
//         })
//         .catch(error => console.log('Erro ao carregar classes: ' + error.message));
// }

// document.addEventListener('DOMContentLoaded', function() {
//     carregarOpcoesClasses('class-select');
// });
document.addEventListener('DOMContentLoaded', () => {
  const raceSelect = document.getElementById('race-select');
 // const classSelect = document.getElementById('class-select');
  const subraceSelect = document.getElementById('subrace-select');
  

  raceSelect.addEventListener('change', () => {
    const raceName = raceSelect.value.split(' (')[0];
    carregarOpcoesSubracas(raceName, 'subrace-select');
  });

  carregarOpcoes('races', 'race-select');
  carregarOpcoesSubracas(raceSelect.value.split(' (')[0], 'subrace-select');
  //carregarOpcoesClasses('class-select');
});