import java.util.Scanner;

class RobotGame {
	public static Grid grid;
	protected Robot robot;
	static Scanner reader;

	public static void main(String[] args) {
		reader = new Scanner(System.in);
		RobotGame currentGame = new RobotGame();
		currentGame.getGridDetails();
		currentGame.getRobotDetails();
		System.out.println("The initial position of robot  is  "+ currentGame.robot.currentPosition);
		System.out.println("The Robot  is facing "+ currentGame.robot.currentDirection);
		currentGame.playGame();
		System.out.println("The final position of robot  is  "+ currentGame.robot.currentPosition);
		System.out.println("The Robot  is facing "+ currentGame.robot.currentDirection);

	}

	// Gets the details of the grid from the User
	public void getGridDetails() {
		System.out.println("Enter no of Rows in the Grid: ");
		int rows = reader.nextInt();
		System.out.println("Enter no of Columns in the Grid: ");
		int columns = reader.nextInt();

		// If Grid Size is Invalid, get the values again
		if (rows < 0 || columns < 0) {
			System.out.println("Grid Size cannot be Negative. Try again. ");
			getGridDetails();
		} else {
			// If Grid Size is valid, create the Grid
			RobotGame.grid = new Grid(columns, rows);
		}

	}

	// Gets the details of the Robot from the User
	void getRobotDetails() {

		// Get the X Position of the Robot
		System.out.println("Enter the initial X axis position of the Robot: ");
		int initialX = reader.nextInt();
		// Get the Y Position of the Robot
		System.out.println("Enter the initial Y axis position of the Robot:");
		int initialY = reader.nextInt();

		// If the position is invalid, get it again, till a valid position is
		// entered
		while (initialX > grid.noOfColumns || initialY > grid.noOfColumns
				|| initialX < 0 || initialY < 0) {
			System.out.println("The Position is out of the Grid. Please Enter a valid position inside the grid. ");

			System.out.println("Enter the initial X axis position of the Robot: ");
			initialX = reader.nextInt();
			System.out.println("Enter the initial Y axis position of the Robot:");
			initialY = reader.nextInt();
		}

		// Get the Direction of the Robot
		System.out.println("Which direction is the Robot Currently facing? \n(N - North, E - East, W - West, S-South): ");
		char direction = reader.next().toLowerCase().charAt(0);

		// If the Direction is not in N,E,W or S for North,East,West or South
		// respectively
		// Prompt for a valid Direction
		while (!("news".indexOf(direction) >= 0)) {
			System.out.print("No Such Direction. Try again ");
			System.out.print("Enter one of the following: \nN - North, E - East, W - West, S-South ");
			direction = reader.next().toLowerCase().charAt(0);
		}

		// Convert the 'char' direction into an 'Enum'
		Direction currentDirection = getDirection(direction);

		// Create the Robot in the entered position and direction
		robot = new Robot(new Position(initialX, initialY), currentDirection);

	}

	public void playGame() {

		// Gets the no of instructions from the User
		System.out.println("Enter number of instructions: ");
		int noOfCommands = reader.nextInt();

		for (int i = 0; i < noOfCommands; i++) {
			// Get the Instruction and Perform it
			getCommand();
		}
	}

	// Prompts the User for a Instruction and performs it
	// An Instruction can be a (M)OVE or a (R)OTATE
	// MOVE - Instructs the robot to move in current for a certain number of
	// steps
	// ROTATE - Instructs the robot to rotate to a specific direction
	public void getCommand() {

		// Get the command
		System.out.println("Give a command to the Robot (M - Move, R- Rotate) :");
		char command = reader.next().toLowerCase().charAt(0);
		switch (command) {
		case 'm':
			// If the command is a MOVE
			// get the number of steps to move
			System.out.print("Enter the number of positions to move ");
			int noOfMoves = reader.nextInt();
			// Save the current position of the Robot and try to move it
			Position p1 = new Position(robot.currentPosition);
			boolean success = move(robot.currentDirection, noOfMoves);
			// If the move fails and the robot cannot be moved
			// restore the original position of the robot
			// and prompt the user for a valid move.
			if (!success) {
				robot.currentPosition = p1;
				System.out.println("Invalid Move. Try again");
				getCommand();
			}
			break;

		// If the command is a ROTATE
		case 'r':
			// Get the direction to rotate to.
			System.out.print("Enter the direction to rotate the Robot: \n(N - North, E - East, W - West, S-South):");
			char direction = reader.next().toLowerCase().charAt(0);
			// Check if the direction is valid
			if ("news".indexOf(direction) >= 0) {
				// rotate the robot
				robot.currentDirection = getDirection(direction);
			} else {
				System.out.print("No Such Direction. Try again ");
				// If the direction is invalid. Ask for a valid input
				getCommand();
			}
			break;

		// If the command is invalid.
		// Prompt for a valid command
		default:
			System.out.println("Invalid Command.\nPlease Enter again.");
			getCommand();
		}
	}

	// Moves the Robot in the specified 'direction' for the specified no of
	// times
	public boolean move(Direction direction, int noOfTimes) {
		try {
			for (int i = 0; i < noOfTimes; i++) {
				switch (direction) {
				case North:
					robot.moveNorth();
					break;
				case East:
					robot.moveEast();
					break;
				case West:
					robot.moveWest();
					break;
				case South:
					robot.moveSouth();
					break;
				default:
					break;
				}
			}
		} catch (InvalidMoveException ime) {
			// If the robot cannot move further
			// return false
			System.out.println(ime.getMessage());
			return false;
		}
		return true;
	}

	// Converts the char code of a Direction into the corresponding Enum
	public Direction getDirection(char direction) {
		switch (direction) {
		case 'n':
			return Direction.North;
		case 's':
			return Direction.South;
		case 'w':
			return Direction.West;
		case 'e':
			return Direction.East;
		}
		// The code below will never get executed
		// but the compiler wants a 'return' statement outside the 'switch'
		// So I gave it one.
		return Direction.North;
	}

}

enum Direction {
	North, West, South, East
}

class Robot {

	protected Position currentPosition = new Position(0, 0);
	protected Direction currentDirection = Direction.North;

	Robot(Position positon, Direction direction) {
		this.currentPosition = positon;
		this.currentDirection = direction;
	}

	void moveWest() throws InvalidMoveException {
		// If you are not on the first column, you can move west, then
		// 			Move West
		// Else
		// 			Throw an Exception
		if (currentPosition.x > 0) {
			this.currentPosition.x--;
		} else {
			throw new InvalidMoveException("Cannot Move West beyond "
					+ currentPosition);
		}
	}

	void moveEast() throws InvalidMoveException {
		// If you are not on the last column, you can move east, then
		// 			Move East
		// Else
		// 			Throw an Exception
		if (currentPosition.x < RobotGame.grid.noOfColumns) {
			this.currentPosition.x++;
		} else {
			throw new InvalidMoveException("Cannot Move East beyond "
					+ currentPosition);
		}
	}

	void moveNorth() throws InvalidMoveException {
		// If you are not on the first row, you can move north, then
		// 			Move North
		// Else
		// 			Throw an Exception		
		if (currentPosition.y > 0) {
			this.currentPosition.y--;
		} else {
			throw new InvalidMoveException("Cannot Move North beyond "
					+ currentPosition);
		}
	}

	void moveSouth() throws InvalidMoveException {
		// If you are not on the last row, you can move South, then
		// 			Move South
		// Else
		// 			Throw an Exception		
		
		if (currentPosition.y < RobotGame.grid.noOfRows) {
			this.currentPosition.y++;
		} else {
			throw new InvalidMoveException("Cannot Move South beyond "
					+ currentPosition);
		}
	}
}

// A class for the Grid in which the Robot will move
// The Grid index starts from (0,0)
// noOfColumns - the extent of X axis in the grid.
// noOfRows - the extent of Y axis in the grid.
class Grid {
	public int noOfColumns;
	public int noOfRows;

	Grid(int columns, int rows) {
		noOfColumns = columns;
		noOfRows = rows;
	}
}

// This Exception gets thrown when the Robot moves out of the Grid
class InvalidMoveException extends Exception {

	public InvalidMoveException(String exceptionMessage) {
		super(exceptionMessage);
	}
}

// A Class for the current position of the Robot
// I made this a separate Class so that,
// 1. It is easier to print the current position of the Robot
// 2. It would be easier to compare the positions of two Robots
// if there a multiple Robots on the Grid.
class Position {
	protected int x = 0;
	protected int y = 0;

	Position(int x, int y) {
		this.x = x;
		this.y = y;
	}

	Position(Position p) {
		if (null != p) {
			this.x = p.x;
			this.y = p.y;
		} else {
			this.x = 0;
			this.y = 0;
		}
	}
	@Override
	public String toString() {
		return " x = " + x + " y = " + y;
	}
}