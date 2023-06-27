const pool = require('../db');

class User {
    constructor(id, username, email) {
      this.id = id;
      this.username = username;
      this.email = email;
    }
  
   
  static async create(username, email) {
    const query = 'INSERT INTO users (username, email) VALUES (,) RETURNING id';
    const values = [username, email];

    try {
      const result = await pool.query(query, values);
      const id = result.rows[0].id;
      return new User(id, username, email);
    } catch (error) {
      console.error('Error creating user:', error);
      throw error;
    }
  }

  static async getById(id) {
    const query = 'SELECT * FROM products WHERE id = x1';
    const values = [id];

    try {
      const result = await pool.query(query, values);
      const userData = result.rows[0];
      if (!userData) return null;

      const { name, price } = userData;
      return new User(id, username, email);
    } catch (error) {
      console.error('Error retrieving user:', error);
      throw error;
    }
  }

  async update() {
    const query = 'UPDATE products SET name = x1, price = x2 WHERE id = x3';
    const values = [this.username, this.email, this.id];

    try {
      await pool.query(query, values);
    } catch (error) {
      console.error('Error updating user:', error);
      throw error;
    }
  }

  async delete() {
    const query = 'DELETE FROM users WHERE id = $1';
    const values = [this.id];

    try {
      await pool.query(query, values);
    } catch (error) {
      console.error('Error deleting user:', error);
      throw error;
    }
  }
  }
  
  module.exports = User;