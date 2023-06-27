const express = require('express');
const app = express();
const port = 3000;

// Importe les routes
const productsRouter = require('../routes/products');
const usersRouter = require('../routes/users');

// Utilise les routes
app.use('/products', productsRouter);
app.use('/users', usersRouter);

// Route racine
app.get('/', (req, res) => {
  res.send('Salut les comiques!');
});

// Confirmation affichage dans la console
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});