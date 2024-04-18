const express = require('express');
const artworkRouter = require('./artwork');
const authRouter = require('./auth');

const router = express.Router();

router.use('/artwork', artworkRouter);
router.use('/auth', authRouter);

module.exports = router;