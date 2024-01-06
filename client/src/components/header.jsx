import React from 'react';
import { AppBar, Toolbar, Typography, Button } from '@mui/material';

const Header = () => {
    const handleLogout = () => {
        // Handle logout logic here
    };

    const name = (window.location.href).split('#')[1];

    return (
        <AppBar position="static" sx={{marginBottom: 2}}>
            <Toolbar>
                <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
                    My App
                </Typography>
                <Typography variant="body1" sx={{ marginRight: 2 }}>
                    {name}
                </Typography>
                <Button color="inherit" onClick={handleLogout}>
                    Logout
                </Button>
            </Toolbar>
        </AppBar>
    );
};

export default Header;
