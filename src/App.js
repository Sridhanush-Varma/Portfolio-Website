import React from 'react';
import { Header, Skills, Education, Projects, Section } from './components';
import './App.css';

function App() {
  return (
    <div className="App">
      <Header />
      <main>
        <Section id="summary">
          <h2>Professional Summary</h2>
          <p>Computer Vision and Image Processing specialist with expertise in Python programming...</p>
        </Section>
        <Skills />
        <Education />
        <Projects />
      </main>
    </div>
  );
}

export default App; 