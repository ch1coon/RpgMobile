function carregarOpcoes(races, idSelect) {
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

  fetch("/data/subraces.json")
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
document.addEventListener("DOMContentLoaded", () => {
  const raceSelect = document.getElementById("race-select");
  const subraceSelect = document.getElementById("subrace-select");

  raceSelect.addEventListener("change", () => {
    const raceName = raceSelect.value.split(" (")[0];
    carregarOpcoesSubracas(raceName, "subrace-select");
  });

  carregarOpcoes("races", "race-select");
  carregarOpcoesSubracas(raceSelect.value.split(" (")[0], "subrace-select");
  //carregarOpcoesClasses('class-select');
});
