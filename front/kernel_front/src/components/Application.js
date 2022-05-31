import Button from '@mui/material/Button';

function Application() {

  const handleSubmit = (e, type) => {
      e.preventDefault();
      let data = {
          cmd: type,
          src:'GUI',
          dst:'APP',
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
  }

  return (
    <div>
        <h1>Applications</h1>
        <Button onClick={(e)=>handleSubmit(e,'run')} variant="outlined" color="success">INICIAR</Button>
        <Button onClick={(e)=>handleSubmit(e,'stop')} variant="outlined" color="warning">DETENER</Button>
    </div>
  );
}
  
export default Application;