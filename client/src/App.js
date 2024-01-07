import { Login } from './pages/login.jsx';
import { Home } from  './pages/home.jsx';
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import React from 'react';
import './App.css';

function App() {
  return (
     <Router>
      <Routes>
        <Route path='/' element={< Login />}/>
        <Route path='/dashboard' element={< Home />}/>
      </Routes>
    </Router>
  )
}

export default App;
