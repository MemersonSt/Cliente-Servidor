import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'

const tasks = ["task 1", "task2", "task 3"]

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App 
      tasks={tasks}
    />
  </React.StrictMode>,
)
