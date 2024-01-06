import { Button, Typography, TextField, Stack } from '@mui/material';

export const Login = () => {
    return (
        <div style={{'height': '100%', 'display': 'flex', 'justifyContent': 'center'}}>
        <Stack spacing={5} marginLeft={2} marginRight={2} justifyContent="center" alignItems="center">
          <Typography variant="h1">
            Welcome to APPNAMEEE!
          </Typography>
          <Typography variant="h3">
            Please enter your username to take studying to the next level!
          </Typography>
          <TextField id="outlined-basic" label="Outlined" variant="outlined"  />
          <Button variant="contained">Log In</Button>
        </Stack>    
    </div>
    )}
    
    export default Login;