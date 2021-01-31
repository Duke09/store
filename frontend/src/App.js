import logo from './pizzalogo.jpeg';
import PizzaList from './pizzerias/pizzerialist'
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Web App for pizza lovers
        </p>
        <h1>
          Pizerria
        </h1>
        <PizzaList/>
      </header>
    </div>
  );
}

export default App;
