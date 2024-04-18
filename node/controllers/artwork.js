const express = require('express');
const Artwork = require('../models').Artwork;

const router = express.Router();

router.get('/', async (req, res) => {
  const allArtwork = await Artwork.findAll();
  return res.json(allArtwork);
})

router.post('/', async (req, res) => {
  // todo: req.body validation
  const newArtwork = await Artwork.create(req.body);
  return res.json(newArtwork);
})

module.exports = router;