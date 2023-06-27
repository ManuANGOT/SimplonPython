const pool = require('../db');

class Product {
  constructor(id, name, price) {
    this.id = id;
    this.name = name;
    this.price = price;
  }

  static async create(name, price) {
    const query = 'INSERT INTO products (name, price) VALUES ($1, $2) RETURNING id';
    const values = [name, price];

    try {
      const result = await pool.query(query, values);
      const id = result.rows[0].id;
      return new Product(id, name, price);
    } catch (error) {
      console.error('Error creating product:', error);
      throw error;
    }
  }

  static async getById(id) {
    const query = 'SELECT * FROM products WHERE id = $1';
    const values = [id];

    try {
      const result = await pool.query(query, values);
      const productData = result.rows[0];
      if (!productData) return null;

      const { name, price } = productData;
      return new Product(id, name, price);
    } catch (error) {
      console.error('Error retrieving product:', error);
      throw error;
    }
  }

  async update() {
    const query = 'UPDATE products SET name = $1, price = $2 WHERE id = $3';
    const values = [this.name, this.price, this.id];

    try {
      await pool.query(query, values);
    } catch (error) {
      console.error('Error updating product:', error);
      throw error;
    }
  }

  async delete() {
    const query = 'DELETE FROM products WHERE id = $1';
    const values = [this.id];

    try {
      await pool.query(query, values);
    } catch (error) {
      console.error('Error deleting product:', error);
      throw error;
    }
  }
}

module.exports = Product;