import './App.css';
import React, { useEffect, useState} from "react";
import { Row, Col, Button } from "react-bootstrap";
import Archives from './components/Archives';
import Application from './components/Application';
import States from './components/States';
import Logs from './components/Logs';

function App() {
  useEffect(() => {
    const initializeServices = async () => {
      const result = await fetch(
        'http://127.0.0.1:8000/initialize/',
        {
          method: 'GET',
          headers:{
            Accept: 'application/json',
          }
        }
      )
      let services = await result.json();
      console.log(services)
    }
    initializeServices();
  }, [])
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
