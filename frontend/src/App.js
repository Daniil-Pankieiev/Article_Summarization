/**
 * Importing necessary modules and components from libraries
 */
import React, { useState } from 'react';
import axios from 'axios';
import { Container, Typography, TextField, Button, CircularProgress } from '@mui/material';

/**
 * Main App component
 * @returns {JSX.Element} The rendered App component
 */
function App() {
  /**
   * State variables for the App component
   */
  const [articleText, setArticleText] = useState('');
  const [summary, setSummary] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  /**
   * Function to handle input change events
   * @param {Event} event - The input change event
   */
  const handleInputChange = (event) => {
    setArticleText(event.target.value);
  };

  /**
   * Function to handle form submission
   * Makes a POST request to the backend to get the summary of the article
   */
  const handleSubmit = async () => {
    if (!articleText.trim()) {
      setError('Please enter some text to summarize.');
      return; // Exit early if text is empty
    }
    const backendUrl = process.env.REACT_APP_BACKEND_URL;
    console.log('Backend URL:', backendUrl);
    setIsLoading(true);
    setError(null); // Clear any previous errors

    try {
      const response = await axios.post(backendUrl + '/summarize', { text: articleText });
      setSummary(response.data.summary); // Access summary from response data
    } catch (error) {
      console.error(error);
      setError('Error summarizing article. Please try again later.');
    } finally {
      setIsLoading(false);
    }
  };

  /**
   * Render the App component
   */
  return (
    <Container maxWidth="md">
      <Typography variant="h4" gutterBottom>
        Article Analyzer
      </Typography>
      <TextField
        label="Enter article text"
        multiline
        rows={4}
        fullWidth
        value={articleText}
        onChange={handleInputChange}
      />
      <Button variant="contained" color="primary" onClick={handleSubmit} disabled={isLoading}>
        Summarize
      </Button>
      {isLoading && <CircularProgress />}
      {error && <Typography color="error">{error}</Typography>}
      {summary && (
        <Typography variant="body1">{summary}</Typography>
      )}
    </Container>
  );
}

/**
 * Exporting the App component as default
 */
export default App;