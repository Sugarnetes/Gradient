import React, { useState, useEffect } from 'react';
import './leaderboard.css'; 

const Leaderboard = () => {
    const [leaderboardData, setLeaderboardData] = useState([]);

    useEffect(() => {
        const ws = new WebSocket('ws://localhost:8888/websocket');
        
        ws.onopen = () => {
            console.log('WebSocket Connected');
        };
        
        ws.onmessage = (event) => {
            const data = JSON.parse(event.data);
            console.log('Hi', data);

            // Loop through each user in the data array and log them
            data.forEach((user) => {
                console.log('User:', user);
            });

            setLeaderboardData(data);
        };
        
        ws.onclose = () => {
            console.log('WebSocket Disconnected');
        };
        
        ws.onerror = (error) => {
            console.error('WebSocket Error: ', error);
        };

        // Cleanup on component unmount
        return () => {
            if (ws) ws.close();
        };
    }, []);

    return (
        <div className="leaderboard">
            <h2>Leaderboard</h2>
            <table>
                <thead>
                    <tr>
                        <th>Rank</th>
                        <th>Name</th>
                        <th>Score</th>
                    </tr>
                </thead>
                <tbody>
                    {leaderboardData.map((entry, index) => (
                        <tr key={entry.rank}>
                            <td>{entry.rank}</td>
                            <td>{entry.username}</td>
                            <td>{entry.points}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default Leaderboard;
