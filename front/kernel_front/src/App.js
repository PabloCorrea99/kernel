import './App.css';
import React from "react";
import { Row, Col } from "react-bootstrap";
import Archives from './components/Archives';
import Application from './components/Application';
import States from './components/States';
import Logs from './components/Logs';

function App() {

  return (
    <div className="App">
      <Row>
        <Col md={6}><Archives/></Col>
        <Col md={6}><Application/></Col>
      </Row>
      <Row>
        <Col md={6}><States/></Col>
        <Col md={6}><Logs/></Col>
      </Row>
    </div>
  );
}

export default App;
