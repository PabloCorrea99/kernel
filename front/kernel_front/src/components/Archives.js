import React from "react";
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';

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
            <TextField id="outlined-basic" label="Outlined" variant="outlined" onChange={handleChange} value={archiveName}/>
            <Button onClick={(e)=>handleSubmit(e,'create')} variant="contained" color="success">CREAR</Button>
            <Button onClick={(e)=>handleSubmit(e,'delete')} variant="contained" color="warning">BORRAR</Button>
      </div>
    );
  }
  
export default Archives;