import { useState } from "react"
import axios from 'axios'
import type { FormEvent } from "react"

function RegForm () {
  const [ userInfo, setUserInfo ] = useState({
    username: '',
    password: '',
  })

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault()
    // TODO: send userInfo to server
    console.log(userInfo)
    try {
      const { data } = await axios.post('/api/auth/register', userInfo)
      console.log(data)
    } catch (err) {
      console.log(err)
    }
  }

  return (
    <form onSubmit={handleSubmit}>
      <div className="mb-3">
        <label
          htmlFor="reg-email"
          className="form-label">
            Email address
        </label>
        <input
          type="email"
          className="form-control"
          id="reg-email"
          value={userInfo.username}
          onChange={e => setUserInfo({ ...userInfo, username: e.target.value })}
        />
      </div>

      <div className="mb-3">
        <label
          htmlFor="reg-email"
          className="form-label">
            Password
        </label>
        <input
          type="password"
          className="form-control"
          id="reg-password"
          value={userInfo.password}
          onChange={e => setUserInfo({ ...userInfo, password: e.target.value })}
        />
      </div>

      <button type="submit" className="btn btn-primary">
        Register
      </button>
    </form>
  )
}

export default RegForm