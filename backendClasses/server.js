const express = require('express');
const app = express();
const port = 3000;

const routes = require('./routes');

app.use(express.static(__dirname + '/..')); // Define a raiz do projeto como pasta estática

app.use('/', routes); // Usa as rotas definidas no arquivo routes.js

app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
