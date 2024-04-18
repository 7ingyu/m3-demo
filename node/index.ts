import 'dotenv/config'
import express from 'express'
import apiRouter from './controllers'

const app = express()
const PORT = process.env.PORT || 3000

app.use(express.json())

app.use('/api', apiRouter)

app.listen(PORT || 3000, () => {
  console.log(`Server running on port ${PORT}`)
})
