const express = require('express');
const Artwork = require('../models').Artwork;

const router = express.Router();

router.get('/', async (req, res) => {
  const allArtwork = await Artwork.findAll();
  return res.json(allArtwork);
})

router.post('/', async (req, res) => {
  // todo: req.body validation
  try {
    const newArtwork = await Artwork.create(req.body);
    return res.json(newArtwork);
  } catch (e) {
    if (e.message.includes('constraint')) {
      return res.status(400).send('Invalid artist ID');
    }
    return res.status(500).send(e.message);
  }
})

module.exports = router;