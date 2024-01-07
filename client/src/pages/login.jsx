import { Button, Typography, TextField, Stack, createTheme, ThemeProvider, Box } from '@mui/material';
import React, { useState } from 'react';

const theme = createTheme({
    typography: {
      allVariants: {
        fontFamily: 'Acme',
        textTransform: 'none',
        marginBottom: '10pt',
      },
    },
  });

export const Login = () => {
    const [username, setUsername] = useState("");
    return (
            <ThemeProvider theme={theme}>
                <Box display="flex" minHeight="100vh" justifyContent="center" alignItems='center'> 
            <Stack spacing={5} alignItems="center"
            sx={{ border: '5px solid black', padding: '5rem', width: 'fit-content' }}>
            <Typography variant="h1">
                Welcome to Gradient
            </Typography>
            <Typography variant="h4" fontStyle="italic">
                Please enter your username to take studying to the next level!
            </Typography>
            <TextField id="outlined-basic" label="Username" variant="outlined" 
                value={username}
                onChange={e => setUsername(e.target.value)} />
            <Button variant="contained" href={"/dashboard#" + username }>Log In</Button>
            </Stack>    
            </Box>
        </ThemeProvider>
    )}
    
    export default Login;