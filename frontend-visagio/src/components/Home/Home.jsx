import './Home.css'
import Header from '../Header/Header'
import SendButton from '../SendButton/SendButton'
import InputNumber from '../InputNumber/InputNumber'
import { useState } from 'react'

function Home() {
  const handleButtonClick = () => {
    // Lógica para envio da avaliação
    console.log("Avaliação enviada!");
  };

  const [formData, setFormData] = useState({
    dono: '',
    resiliencia: '',
    organizacao: '',
    aprender: '',
    teamPlayer: '',
    qualidade: '',
    prazos: '',
    maisComMenos: '',
    foraDaCaixa: '',
  })

  const handleChange = (e) => {
    const { name, value } = e.target
    setFormData({ ...formData, [name]: value })
  }

  return (
    <div className="home-container">
      <Header />
      <div className="form-wrapper">
        <h2>Autoavaliação</h2>

        <label htmlFor="usuario">Nome do Usuário:</label>
        <select id="usuario" name="usuario">
          <option>João Silva</option>
          <option>Maria Oliveira</option>
          <option>Carlos Souza</option>
        </select>

        <h3>Critérios Comportamentais (1 a 5)</h3>
        <InputNumber label="Sentimento de Dono:" name="dono" value={formData.dono} onChange={handleChange} />
        <InputNumber label="Resiliência nas Adversidades:" name="resiliencia" value={formData.resiliencia} onChange={handleChange} />
        <InputNumber label="Organização no Trabalho:" name="organizacao" value={formData.organizacao} onChange={handleChange} />
        <InputNumber label="Capacidade de Aprender:" name="aprender" value={formData.aprender} onChange={handleChange} />
        <InputNumber label={`Ser "Team Player":`} name="teamPlayer" value={formData.teamPlayer} onChange={handleChange} />

        <h3>Critérios de Execução (1 a 5)</h3>
        <InputNumber label="Entregar com Qualidade:" name="qualidade" value={formData.qualidade} onChange={handleChange} />
        <InputNumber label="Atender aos Prazos:" name="prazos" value={formData.prazos} onChange={handleChange} />
        <InputNumber label="Fazer mais com Menos:" name="maisComMenos" value={formData.maisComMenos} onChange={handleChange} />
        <InputNumber label="Pensar Fora da Caixa:" name="foraDaCaixa" value={formData.foraDaCaixa} onChange={handleChange} />

        {/* Botão customizado */}
        <button className="submit-button" onClick={handleButtonClick}>Enviar Avaliação</button>
      </div>
    </div>
  )
}

export default Home;
