import React from "react";
import { Button } from "react-bootstrap";

function Archives() {
    const [archiveName, setArchiveName] = React.useState('');

    const handleChange = (e) => {
        setArchiveName(e.target.value);
    }

    const handleSubmit = (e, type) => {
        e.preventDefault();
        let data = {
            cmd: type,
            src:'GUI',
            dst:'GestorArc',
            msg: archiveName
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
                  console.log("Respuesta: ", response);
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
        setArchiveName('');
    }

    return (
      <div>
          <h1>Archives</h1>
            <input
                onChange={handleChange}
                value={archiveName}
                placeholder="Escribe un mensaje..."
                type="text"
            />
            <Button onClick={(e)=>handleSubmit(e,'creat')} variant="success">CREAR</Button>
            <Button onClick={(e)=>handleSubmit(e,'delete')} variant="warning">BORRAR</Button>
      </div>
    );
  }
  
export default Archives;