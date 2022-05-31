import './App.css';
import React from "react";
import Archives from './components/Archives';
import Application from './components/Application';
import States from './components/States';
import Logs from './components/Logs';
import { styled } from '@mui/material/styles';
import Paper from '@mui/material/Paper';
import Grid from '@mui/material/Grid';

const Item = styled(Paper)(({ theme }) => ({
  backgroundColor: theme.palette.mode === 'dark' ? '#1A2027' : '#fff',
  ...theme.typography.body2,
  padding: theme.spacing(1),
  textAlign: 'center',
  color: theme.palette.text.secondary,
}));
function App() {

  return (
    <>
    <Grid container spacing={2}>
      <Grid item xs={6}>
        <Item><Archives/></Item>
      </Grid>
      <Grid item xs={6}>
        <Item><Application/></Item>
      </Grid>
      <Grid item xs={6}>
        <Item><States/></Item>
      </Grid>
      <Grid item xs={6}>
        <Item><Logs/></Item>
      </Grid>
    </Grid>
    <h5>Created By: Pablo Correa and Felipe Alvarez</h5>
    </>
  );
}

export default App;
