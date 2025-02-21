import React from 'react';
import { motion } from 'framer-motion';

const Projects = () => {
  const projects = [
    {
      title: "Image Processing Suite",
      details: [
        "Developed algorithms for image dilation and erosion",
        "Implemented morphological gradient detection",
        "Created facial recognition system with live camera integration"
      ],
      technologies: ["Python", "OpenCV", "NumPy"],
      github: "https://github.com/Sridhanush-Varma/Image-Processing-Suite.git"
    },
    {
      title: "ChatBot using Python",
      details: [
        "Developed a basic chatbot using Python",
        "Implemented a chatbot using NLTK library",
        "Created a chatbot that can answer questions and help with tasks",
        "Created the chatbot using speech technology"
      ],
      technologies: ["Python", "NLTK", "Speech Recognition"],
      github: "https://github.com/Sridhanush-Varma/Chatbot.git"
    }
  ];

  const containerVariants = {
    hidden: { opacity: 0 },
    visible: { 
      opacity: 1,
      transition: { staggerChildren: 0.2 }
    }
  };

  const projectVariants = {
    hidden: { y: 20, opacity: 0 },
    visible: { 
      y: 0, 
      opacity: 1,
      transition: { duration: 0.5 }
    }
  };

  return (
    <motion.section 
      className="section"
      variants={containerVariants}
      initial="hidden"
      animate="visible"
    >
      <h2>Projects</h2>
      <div className="projects-container">
        {projects.map((project, index) => (
          <motion.div
            key={index}
            className="project-item"
            variants={projectVariants}
          >
            <h3>{project.title}</h3>
            <ul>
              {project.details.map((detail, i) => (
                <motion.li
                  key={i}
                  initial={{ opacity: 0, x: -20 }}
                  animate={{ opacity: 1, x: 0 }}
                  transition={{ delay: i * 0.1 }}
                >
                  {detail}
                </motion.li>
              ))}
            </ul>
            <div className="project-technologies">
              {project.technologies.map((tech, i) => (
                <span key={i} className="technology-tag">
                  {tech}
                </span>
              ))}
            </div>
            <a 
              href={project.github} 
              target="_blank" 
              rel="noopener noreferrer"
              className="github-link"
            >
              View on GitHub
            </a>
          </motion.div>
        ))}
      </div>
    </motion.section>
  );
};

export default Projects; 