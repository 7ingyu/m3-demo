const express = require('express');
const router = express.Router();
const bcrypt = require('bcrypt');
const User = require('../models').User;

const saltRounds = process.env.SALT_ROUNDS || 10;

router.get('/', (req, res) => {
  return res.send('auth here');
})

router.post('/register', async (req, res) => {
  // todo: req.body validation
  const username = req.body.username;
  const existingUser = await User.findOne({ where: { username } });
  if (existingUser) {
    return res.status(400).send('User already exists');
  }
  try {
    const hash = await bcrypt.hash(req.body.password, saltRounds)
    const newUser = await User.create({
      ...req.body,
      password: hash,
    });
    return res.send({
      ...newUser.dataValues, password: '[hidden]'
    });
  } catch (error) {
    return res.status(500).send('Error hashing password');
  }
})

module.exports = router;