import { BrowserRouter as Router, Routes, Route, useNavigate } from 'react-router-dom'
import './App.css'
import Socio from './components/Socio/Socio'
import Home from './components/Home/Home'

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/colaborador" element={<Home />} />
        <Route path="/socio" element={<Socio />} />
      </Routes>
    </Router>
  )
}

export default App
