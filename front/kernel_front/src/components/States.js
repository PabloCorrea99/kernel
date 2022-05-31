import React, {useEffect} from 'react';
import Button from '@mui/material/Button';

function States() {
  const [systemStates, setSystemStates] = React.useState([])
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
      setSystemStates(services)
    }
    initializeServices();
  }, [])
  const handleExit = () => {
    try {
      fetch("http://127.0.0.1:8000/exit/", {
        method: "GET",
        headers: {
          "Content-type": "application/json",
        },
      }).then((data) =>
        data.json().then((response) => {
          if (data.status >= 200 && data.status < 300) {
          } else if (data.status >= 300 && data.status <= 404) {
            console.log("ERROR DE BUSQUEDA: ", data);
          } else {
            window.alert("SYSTEM TERMINATED");
          }
        })
      );
    } catch (error) {
      window.alert("SYSTEM TERMINATED");
    }
  }
  const handleSubmit = (e, type) => {
    e.preventDefault();
    let data = {
        cmd: type,
        src:'GUI',
        dst:'kernel',
        msg: ''
      };
    let msg = JSON.stringify(data);
    console.log(msg)
    try {
        fetch("http://127.0.0.1:8000/action/", {
          method: "PUT",
          headers: {
            "Content-type": "application/json",
          },
          body: msg,
        }).then((data) =>
          data.json().then((response) => {
            if (data.status >= 200 && data.status < 300) {
              console.log("RESPONSE: ",response)
              setSystemStates(response)
              //handleExit()
            } else if (data.status >= 300 && data.status <= 404) {
              console.log("ERROR DE BUSQUEDA: ", data);
            } else {
              console.log("ERROR DE SERVIDOR: ", data);
            }
          })
        );
      } catch (error) {
        console.log(error);
    }
  }
    return (
      <div>
          <h1>States</h1>
          {systemStates.map((state)=>(
            <ul>
              <li><h3>Kernel: {state.kernel_state}</h3></li>
              <li><h3>GUI: {state.kernel_state}</h3></li>
              <li><h3>Archives: {state.kernel_state}</h3></li>
              <li><h3>Applications: {state.kernel_state}</h3></li>
            </ul>
          ))}
          <Button variant="outlined" color="error" onClick={(e)=>handleSubmit(e,'exit')} >DETENER SISTEMA</Button>
      </div>
    );
  }
  
export default States;