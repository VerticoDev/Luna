import json

class MemorySystem:
    def __init__(self, config):
        self.config = config
        self.memory = {
            'episodic': [],
            'semantic': [],
            'procedural': [],
            'generative': []
        }

    # Simulate storing episodic memory (event data)
    def store_episodic_memory(self, event_data):
        self.memory['episodic'].append(event_data)

    # Simulate storing semantic memory (conceptual relationships)
    def store_semantic_memory(self, concept_data):
        self.memory['semantic'].append(concept_data)

    # Simulate storing procedural memory (operational knowledge)
    def store_procedural_memory(self, operation_data):
        self.memory['procedural'].append(operation_data)

    # Simulate storing generative memory (creative ideas)
    def store_generative_memory(self, creative_data):
        self.memory['generative'].append(creative_data)

    # Save memory to file (for persistence)
    def save_memory(self, file_path):
        with open(file_path, 'w') as f:
            json.dump(self.memory, f, indent=4)

    # Load memory from file
    def load_memory(self, file_path):
        with open(file_path, 'r') as f:
            self.memory = json.load(f)

    def display_memory(self):
        print(json.dumps(self.memory, indent=4))


# Example usage
if __name__ == "__main__":
    config = {'memory_save_path': 'memory.json'}
    memory_system = MemorySystem(config)

    # Simulate storing different types of memory
    memory_system.store_episodic_memory('Event: Market surge')
    memory_system.store_semantic_memory('Concept: Trend analysis')
    memory_system.store_procedural_memory('Operation: Buy 10 units')
    memory_system.store_generative_memory('Creative: New trading strategy')

    # Display and save memory
    memory_system.display_memory()
    memory_system.save_memory(config['memory_save_path'])
