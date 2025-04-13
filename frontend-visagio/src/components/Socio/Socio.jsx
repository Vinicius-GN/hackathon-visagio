import Header from "../Header/Header"
import "./Socio.css"
import { useState } from "react"

const avaliacoesMock = {
    "João Silva": [4.2, 3.8, 4.0],
    "Maria Oliveira": [3.2, 3.5, 3.1],
    "Carlos Souza": [4.8, 4.7, 5.0]
  }
  
  const getMensagemDesempenho = (media) => {
    if (media >= 4.5) return "Superou Expectativas"
    if (media >= 4.0) return "Entregou com Excelência"
    if (media >= 3.0) return "Fez o Básico"
    return "Abaixo do Esperado"
  }

const Socio = () => {
    const [colaborador, setColaborador] = useState("")
    const avaliacoes = colaborador ? avaliacoesMock[colaborador] || [] : []
    const media =
        avaliacoes.length > 0
        ? (avaliacoes.reduce((a, b) => a + b, 0) / avaliacoes.length).toFixed(2)
        : null
  return (
    <div className="socio-container">
      <Header />
        <div className="form-wrapper">
        <h2>Painel do Sócio</h2>

        <label htmlFor="colaborador">Selecionar Colaborador:</label>
        <select
            id="colaborador"
            name="colaborador"
            value={colaborador}
            onChange={(e) => setColaborador(e.target.value)}
        >
            <option value="">-- Selecione --</option>
            <option>João Silva</option>
            <option>Maria Oliveira</option>
            <option>Carlos Souza</option>
        </select>

        {colaborador && (
            <div style={{ marginTop: "20px" }}>
            <h3>Histórico de Avaliações ({colaborador})</h3>
            <p>Avaliações: {avaliacoes.join(", ")}</p>
            <button className="media-button">
                Média: {media} - {getMensagemDesempenho(media)}
            </button>
            </div>
        )}
        </div>
    </div>
  )
}

export default Socio
