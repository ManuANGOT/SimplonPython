const cacheNoStore = require('./middleware/cacheNoStore.js')
module.exports = () => {
   router.get('/:id', cacheNoStore, controllers.getProduct)
}