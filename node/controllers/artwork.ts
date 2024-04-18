import express from 'express';
const router = express.Router();

router.get('/', (req, res) => {
  return res.send('artworks here');
})

export default router;