'use strict';
const {
  Model
} = require('sequelize');
module.exports = (sequelize, DataTypes) => {
  class Artwork extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate({User}) {
      // define association here
      Artwork.belongsTo(User, {foreignKey: 'artist'})
    }
  }
  Artwork.init({
    title: DataTypes.STRING,
    price: DataTypes.DECIMAL,
    medium: DataTypes.STRING,
    artist: {
      type: DataTypes.INTEGER,
      references: 'users',
      referencesKey: 'id',
    }
  }, {
    sequelize,
    modelName: 'artwork',
  });
  return Artwork;
};