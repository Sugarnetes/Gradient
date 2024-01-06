import { InputLabel, FormControl, Typography,Input, Stack } from '@mui/material';

export const Initial = () => {
  return (
    <div style={{'height': '100%', 'display': 'flex',
    'justifyContent': 'center'}}>
    <Stack spacing={5} marginLeft={2} marginRight={2} justifyContent="center" alignItems="center"
      style={{"height": "100%"}}>

      <Typography variant="h1">
        Welcome to APPNAMEEE!
      </Typography>
      <Typography variant="h3">
        Please enter your username to take studying to the next level!
      </Typography>
      <FormControl>
        <InputLabel htmlFor="my-input">Username</InputLabel>
        <Input id="my-input" aria-describedby="my-helper-text" />
      </FormControl>
      </Stack>
      </div>
  );
}

export default Initial;
