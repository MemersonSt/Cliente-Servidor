import './App.css'

function App({ tasks }) {

  return (
    <div>
      <h1>Lista de Tareas</h1>
      <ul>
          {tasks.map((task, index) => (
            <li key={index}>{task}</li>
          ))}
      </ul>
    </div>
  )
}

export default App
