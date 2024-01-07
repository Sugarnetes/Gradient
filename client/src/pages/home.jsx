import React from 'react';
import Header from '../components/header';
import Upload from '../components/upload';
import Timer from '../components/timer';
import { styled } from '@mui/material/styles';
import Paper from '@mui/material/Paper';
import Grid from '@mui/material/Grid';
import './style.css';
import Leaderboard from '../components/leaderboard';

export const Home = () => {

    const name = (window.location.href).split('#')[1];

    return (
        <div>
        <Header/>  {/* Assuming you have a header component to apply styles */}

        <div className="home_layout">
            <Grid container spacing={2} style={{ height: '100%' }}>

                {/* Left Column */}
                <Grid item xs={2.5} className='Grid-item'>
                    <Grid container direction="column" spacing={2} style={{ height: '100%' }}>
                    
                        {/* Left Column - First Box */}
                        <Grid item xs style={{ height: '100%' }}>
                            <Paper className='Paper'>
                                <Leaderboard />
                            </Paper>
                        </Grid>

                    </Grid>
                </Grid>

                {/* Middle Column */}
                <Grid item xs={6.5} className='Grid-item'>
                    <Grid item xs style={{ height: '100%' }}>
                        <Paper className='Paper'>
                            <div className='center'>
                                <h1>Welcome to Gradient, {name}!</h1>
                                <h3>Let's get studying!</h3>
                            </div>
                        </Paper>
                    </Grid>
                </Grid>

                {/* Right Column */}
                <Grid item xs={3} className='Grid-item'>
                    <Grid container direction="column" spacing={2} style={{ height: '100%' }}>
                    
                        {/* Right Column - First Box */}
                        <Grid item xs style={{ height: '100%' }}>
                            <Paper className='Paper'>
                                <Timer />
                            </Paper>
                        </Grid>
                        
                        {/* Right Column - Second Box */}
                        <Grid item xs style={{ height: '100%' }}>
                            <Paper className='Paper'>
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
