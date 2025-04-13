import './InputNumber.css'

const InputNumber = ({ label, name, value, onChange }) => {
  return (
    <div className="input-number-group">
      <label htmlFor={name}>{label}</label>
      <input
        type="number"
        id={name}
        name={name}
        min="1"
        max="5"
        value={value}
        onChange={onChange}
      />
    </div>
  )
}

export default InputNumber
