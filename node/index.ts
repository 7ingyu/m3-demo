import 'dotenv/config'
import express from 'express'

const app = express()
const PORT = process.env.PORT || 3000

app.use(express.json())

app.get('/', (req, res) => {
  return res.send('hello')
})

app.listen(PORT || 3000, () => {
  console.log(`Server running on port ${PORT}`)
})
