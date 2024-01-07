import React, { useState, useEffect } from 'react';
import './leaderboard.css'; 

const Leaderboard = () => {
    // Test data for the leaderboard

    /*
    const testData = [
        { rank: 1, name: 'Alice', score: 500 },
        { rank: 2, name: 'Bob', score: 400 },
        { rank: 3, name: 'Charlie', score: 300 },
    ];
    */

    const [leaderboardData, setLeaderboardData] = useState([]);

    // Connect to the WebSocket when the component mounts
    useEffect(() => {
        const ws = new WebSocket('ws://localhost:8888/websocket'); // Corrected URL
        ws.onmessage = (event) => {
            const data = JSON.parse(event.data);
            setLeaderboardData(data);
        };
        // Cleanup on component unmount
        return () => {
            ws.close();
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
