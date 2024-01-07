import React from 'react';
import Header from '../components/header';
import Upload from '../components/upload';
import Timer from '../components/timer';
import { styled } from '@mui/material/styles';
import Paper from '@mui/material/Paper';
import Grid from '@mui/material/Grid';
import './style.css';

export const Home = () => {

    const name = (window.location.href).split('#')[1];

    return (
        <div>
            <Header margin='20'/>
            <div className="home_layout">
            <Grid container spacing={2} style={{ height: '100%' }}>

            {/* Left Column */}
            <Grid item xs={3}>
                <Grid container direction="column" spacing={2} style={{ height: '100%' }}>
                
                {/* Left Column - First Box */}
                <Grid item xs>
                    <Paper style={{ height: '100%', backgroundColor: '#eee' }}>
                        Leaderboard
                    </Paper>
                </Grid>

                </Grid>
            </Grid>

            {/* Middle Column */}
            <Grid item xs={6}>
                <Paper style={{ height: '98%', backgroundColor: '#eee' }}>
                      Summary + download button
                </Paper>
            </Grid>

            {/* Right Column */}
            <Grid item xs={3}>
                <Grid container direction="column" spacing={2} style={{ height: '100%' }}>
                
                {/* Right Column - First Box */}
                <Grid item xs>
                    <Paper style={{ height: '100%', backgroundColor: '#eee' }}>
                        <Timer />
                    </Paper>
                </Grid>
                
                {/* Right Column - Second Box */}
                <Grid item xs>
                    <Paper style={{ height: '100%', backgroundColor: '#eee' }}>
                        <Upload/>
                    </Paper>
                </Grid>
                </Grid>
            </Grid>
            </Grid>
        </div>
        </div>
    );
}

export default Home;
