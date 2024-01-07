import React, { useState, useEffect } from 'react';
import './leaderboard.css'; 

const Leaderboard = () => {
    // Test data for the leaderboard
    const testData = [
        { rank: 1, name: 'Alice', score: 500 },
        { rank: 2, name: 'Bob', score: 400 },
        { rank: 3, name: 'Charlie', score: 300 },
        // ... more test data
    ];

    const [leaderboardData, setLeaderboardData] = useState(testData);

    // Placeholder for WebSocket connection setup
    const setupWebSocket = () => {
        // This method will be used to set up the WebSocket connection
        // and listen for messages that contain the leaderboard data.
        // For example:
        // const ws = new WebSocket('ws://localhost:8888/leaderboard');
        // ws.onmessage = (event) => {
        //     const data = JSON.parse(event.data);
        //     setLeaderboardData(data);
        // };
    };

    // Connect to the WebSocket when the component mounts
    useEffect(() => {
        setupWebSocket();
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
                        <tr key={index}>
                            <td>{entry.rank}</td>
                            <td>{entry.name}</td>
                            <td>{entry.score}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default Leaderboard;
