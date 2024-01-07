import { Button, Typography, TextField, Stack } from '@mui/material';
import React, { useState } from 'react';

export const Login = () => {
    const [username, setUsername] = useState("");
    return (
        <div style={{'height': '100%', 'display': 'flex', 'justifyContent': 'center'}}>
            <Stack spacing={5} marginLeft={2} marginRight={2} justifyContent="center" alignItems="center">
            <Typography variant="h1">
                Welcome to APPNAMEEE!
            </Typography>
            <Typography variant="h3">
                Please enter your username to take studying to the next level!
            </Typography>
            <TextField id="outlined-basic" label="Outlined" variant="outlined" 
                value={username}
                onChange={e => setUsername(e.target.value)} />
            <Button variant="contained" href={"/dashboard#" + username }>Log In</Button>
            </Stack>    
        </div>
    )}
    
    export default Login;