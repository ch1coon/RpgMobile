const express = require('express');
const fs = require('fs');
const path = require('path');

const router = express.Router();

router.get('/classes', (req, res) => {
  const classesPath = path.join(__dirname, '..', 'data', 'class'); // Ajuste o caminho para acessar a pasta "data"
  fs.readdir(classesPath, (err, files) => {
    if (err) {
      console.error('Erro ao ler a pasta "class":', err);
      res.status(500).json({ error: 'Erro ao ler a pasta "class"' });
    } else {
      const classNames = files
  .filter((file) => file.startsWith('class-') && file !== 'class-generic.json')
  .map((file) => file.replace('.json', '').replace('class-', ''));



      res.json({ classes: classNames });
    }
  });
});

module.exports = router;
