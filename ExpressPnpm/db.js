const { Pool } = require('pg');

// Configuration de la connexion à PostgreSQL
const pool = new Pool({
  user: 'your_username',
  host: 'your_host',
  database: 'your_database',
  password: 'your_password',
  port: 5432, // Port par défaut pour PostgreSQL
});

module.exports = pool;